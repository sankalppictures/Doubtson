# logic_solver.py
import re

def solve_logic_problem(extracted_text):
    """
    Analyzes the extracted text and provides a logic-based answer.
    This function simulates fetching answers from a GitHub repository
    or applying predefined rules based on the question.

    Args:
        extracted_text (str): The text extracted from the question image.

    Returns:
        str: The answer to the question, or a message if no answer is found.
    """
    # Convert extracted text to lowercase for case-insensitive matching
    query_text = extracted_text.lower().strip()

    # --- Simulate a Knowledge Base from a GitHub Repo ---
    # In a real scenario, you would:
    # 1. Clone/download a specific GitHub repository containing your Q&A data.
    # 2. Parse the files (e.g., Markdown, JSON, CSV) in that repository.
    # 3. Load the questions and answers into a data structure like this dictionary.
    #    For simplicity, we're hardcoding a few examples here.
    #    The keys are keywords/phrases to match, and values are the answers.

    knowledge_base = {
        "भारत की राजधानी": "भारत की राजधानी नई दिल्ली है।",
        "सूर्य क्या है": "सूर्य एक तारा है जो सौरमंडल के केंद्र में स्थित है।",
        "पानी का रासायनिक सूत्र": "पानी का रासायनिक सूत्र H₂O है।",
        "पृथ्वी पर सबसे ऊंचा पर्वत": "पृथ्वी पर सबसे ऊंचा पर्वत माउंट एवरेस्ट है।",
        "कंप्यूटर क्या है": "कंप्यूटर एक इलेक्ट्रॉनिक उपकरण है जो डेटा को संसाधित करता है।",
        "प्रकाश संश्लेषण": "प्रकाश संश्लेषण वह प्रक्रिया है जिसके द्वारा हरे पौधे सूर्य के प्रकाश का उपयोग करके अपना भोजन बनाते हैं।",
        "गणतंत्र दिवस कब मनाया जाता है": "भारत में गणतंत्र दिवस हर साल 26 जनवरी को मनाया जाता है।",
        "आजादी कब मिली": "भारत को 15 अगस्त 1947 को आजादी मिली थी।",
        "सबसे बड़ा महासागर": "प्रशांत महासागर पृथ्वी पर सबसे बड़ा और सबसे गहरा महासागर है।"
    }

    # --- Simple Logic for Matching ---
    # We'll iterate through the knowledge base and check if any key (question/keyword)
    # is present in the extracted query text.
    # This is a very basic matching. For more complex scenarios, you'd use:
    # - Regular expressions for pattern matching
    # - Natural Language Processing (NLP) techniques (e.g., tokenization, stemming, lemmatization)
    # - Semantic search (finding meaning, not just keywords)
    # - Embeddings and vector databases for similarity search (more advanced, but still no OpenAI if using open-source models)

    for question_keyword, answer in knowledge_base.items():
        # Use re.search for more flexible matching (e.g., partial words, word boundaries)
        # re.escape makes sure special characters in question_keyword are treated literally
        if re.search(r'\b' + re.escape(question_keyword) + r'\b', query_text):
            return answer

    # If no match is found, try to provide a generic response or suggest more details
    if "क्या है" in query_text or "क्या होता है" in query_text:
        return "मुझे आपके प्रश्न का सटीक उत्तर नहीं मिल पा रहा है। क्या आप अधिक विशिष्ट जानकारी प्रदान कर सकते हैं?"
    elif "कब" in query_text or "दिनांक" in query_text:
        return "मुझे इस घटना की तारीख के बारे में जानकारी नहीं है। कृपया प्रश्न को और स्पष्ट करें।"
    elif "कौन" in query_text or "किसने" in query_text:
        return "मुझे इस व्यक्ति के बारे में जानकारी नहीं है। कृपया प्रश्न को और स्पष्ट करें।"
    
    return "क्षमा करें, मुझे आपके प्रश्न का उत्तर नहीं मिल पा रहा है। कृपया सुनिश्चित करें कि प्रश्न स्पष्ट है या किसी और तरीके से पूछने का प्रयास करें।"

if __name__ == '__main__':
    # Example Usage for testing
    print("--- Testing Logic Solver ---")

    # Test cases
    test_questions = [
        "भारत की राजधानी क्या है?",
        "सूर्य क्या होता है?",
        "पानी का रासायनिक सूत्र क्या है?",
        "पृथ्वी पर सबसे ऊंचा पर्वत कौन सा है?",
        "कंप्यूटर क्या है?",
        "प्रकाश संश्लेषण की प्रक्रिया क्या है?",
        "भारत में गणतंत्र दिवस कब मनाया जाता है?",
        "भारत को आजादी कब मिली?",
        "सबसे बड़ा महासागर कौन सा है?",
        "आज मौसम कैसा है?", # No direct answer in KB
        "एक नया प्रश्न", # No direct answer in KB
        "यह क्या है?" # Generic "क्या है" match
    ]

    for q in test_questions:
        print(f"\nप्रश्न: {q}")
        answer = solve_logic_problem(q)
        print(f"उत्तर: {answer}")

    print("\n--- End of Testing ---")

