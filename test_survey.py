from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly"""
    question = "What language do you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("English")
    assert "English" in language_survey.answers

def test_store_three_responses():
    """Test that three individual langues will be store"""
    question = "What language do you first learn to speak?"
    answers = ["English", "Spanish", "Mandarin"]
    language_survey = AnonymousSurvey(question)
    for response in answers:
        language_survey.store_response(response)
    
    for response in answers:
        assert response in language_survey.answers
