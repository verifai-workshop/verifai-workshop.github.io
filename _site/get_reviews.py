import openreview
import csv
import os

username = os.getenv('OR_USERNAME')
password = os.getenv('OR_PASSWORD')

# API V2
client = openreview.api.OpenReviewClient(
    baseurl='https://api2.openreview.net',
    username=username, #<your username>',
    password=password, # <your password>'
)

venue_id = "ICLR.cc/2025/Workshop/VerifAI"
venue_group = client.get_group(venue_id)
submission_name = venue_group.content['submission_name']['value']
submissions = client.get_all_notes(invitation=f'{venue_id}/-/{submission_name}', details='replies')

review_name = venue_group.content['review_name']['value']

# Group reviews by submission
paper_reviews = {}

for submission in submissions:
    paper_id = submission.id
    # Try to get the paper title from submission; if missing, do a lookup.
    paper_title = submission.content.get('title', {}).get('value', '')
    if not paper_title:
        paper_note = client.get_note(id=paper_id)
        paper_title = paper_note.content.get('title', {}).get('value', '')
    
    reviews = []
    # Loop over the replies (reviews) for each submission
    for reply in submission.details.get('replies', []):
        # Check if the review invitation matches the expected pattern.
        if f'{venue_id}/{submission_name}{submission.number}/-/{review_name}' in reply.get('invitations', []):
            reviews.append(openreview.api.Note.from_json(reply))
    
    paper_reviews[paper_id] = {
        'paper_title': paper_title,
        'reviews': reviews
    }

# Sort papers based on their ids (or choose another order if needed)
paper_ids = list(paper_reviews.keys())
paper_ids.sort()

# Assign organizers based on the quarter position of each paper.
num_papers = len(paper_ids)
quarter = num_papers // 4
organizers = ['celine', 'wenting', 'theo', 'ameesh']
assignments = {}

for idx, paper_id in enumerate(paper_ids):
    if idx < quarter:
        organizer = organizers[0]
    elif idx < quarter * 2:
        organizer = organizers[1]
    elif idx < quarter * 3:
        organizer = organizers[2]
    else:
        organizer = organizers[3]
    assignments[paper_id] = organizer

# Open CSV file for writing
with open('reviews.csv', 'w', newline='') as outfile:
    csvwriter = csv.writer(outfile, delimiter=',')
    # Write header row
    header = ['paper id', 'paper title', 
              'review 1 title', 'review 1', 'review 1 rating', 'review 1 confidence', 
              'review 2 title', 'review 2', 'review 2 rating', 'review 2 confidence', 
              'organizer']
    csvwriter.writerow(header)
    
    # Write each paper's data row
    for paper_id in paper_ids:
        data = paper_reviews[paper_id]
        reviews = data['reviews']
        # Ensure exactly two reviews per paper; if less, pad with empty values.
        if len(reviews) < 2:
            reviews += [None] * (2 - len(reviews))
        
        # Helper function to extract review details
        def extract_review_details(review):
            if review:
                r_title = review.content.get('title', {}).get('value', '')
                r_text = review.content.get('review', {}).get('value', '')
                r_rating = review.content.get('rating', {}).get('value', '')
                r_conf = review.content.get('confidence', {}).get('value', '')
                return [r_title, r_text, r_rating, r_conf]
            else:
                return ['', '', '', '']
        
        review1 = extract_review_details(reviews[0])
        review2 = extract_review_details(reviews[1])
        
        row = [paper_id, data['paper_title']] + review1 + review2 + [assignments[paper_id]]
        csvwriter.writerow(row)

