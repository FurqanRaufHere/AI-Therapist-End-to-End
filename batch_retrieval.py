import csv
import os
from rag_query_system import retrieve_relevant_chunks  # Import your retrieval fn

# Define your batch queries here (add 20-30 representative queries)
test_queries = [
    "How can I improve my study habits?",
    "What are effective time management strategies for students?",
    "How can I reduce stress and anxiety during exams?",
    "What are some tips for maintaining a healthy work-life balance in college?",
    "How do I stay motivated throughout the semester?",
    "What are good ways to improve my sleep?",
    "I feel anxious about my grades, what should I do?",
    "How do I cope with loneliness at university?",
    "Tips for dealing with social anxiety",
    "How can I build self-confidence?",
    "What should I do if I feel burned out?",
    "How do I overcome procrastination?",
    "How to balance studies and personal life?",
    "What are some relaxation techniques?",
    "How can mindfulness help with anxiety?",
    "What should I eat to reduce stress?",
    "How do I handle peer pressure?",
    "What is imposter syndrome and how to deal with it?",
    "How do I talk to someone about my mental health?",
    "What are signs of depression I should watch for?",
    "How to deal with family expectations?",
    "What are some healthy coping mechanisms?",
    "How can I improve my focus and concentration?",
    "How to handle academic failure?",
    "What resources are available for mental health support?",
    "How do I practice self-care during busy semesters?",
    "What is cognitive behavioral therapy?",
    "How to deal with panic attacks?",
    "How can I improve my time management skills?",
    "How to stay motivated during tough times?",
    "What should I do if I feel overwhelmed?",
    "How to build resilience?",
    "How can I reduce anxiety before presentations?",
    "What techniques help with emotional regulation?",
    "How do I maintain a positive mindset?",
    "How to handle stress related to group projects?",
    "How to avoid burnout in college?",
    "How can exercise improve mental health?",
    "How do I deal with rejection and criticism?",
    "What are grounding techniques for anxiety?",
    "How can journaling help mental health?",
    "How to cope with homesickness?",
    "How to deal with relationship stress?",
    "What are the effects of sleep deprivation on mental health?",
    "How to practice gratitude daily?",
    "How do I find a good therapist?",
    "How can I support a friend with mental health issues?",
    "What is the importance of setting boundaries?",
    "How do I deal with negative thoughts?",
    "How to improve communication skills?",
    "What are some signs of anxiety disorders?",
    "How can I build healthy habits?",
    "What is the role of nutrition in mental health?",
    "How to manage financial stress as a student?"

]

OUTPUT_CSV = "retrieval_for_labeling.csv"

def run_batch_and_save():
    file_exists = os.path.isfile(OUTPUT_CSV)
    with open(OUTPUT_CSV, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Query", "Rank", "SimilarityScore", "RetrievedChunkPreview"])

        for query in test_queries:
            retrieved = retrieve_relevant_chunks(query)
            for rank, item in enumerate(retrieved, start=1):
                preview = item['chunk'][:120].replace('\n', ' ').strip()
                writer.writerow([query, rank, f"{item['score']:.4f}", preview])
            print(f"[✓] Processed query: '{query}'")

if __name__ == "__main__":
    run_batch_and_save()
    print(f"[✓] Retrieval results saved in {OUTPUT_CSV}")
