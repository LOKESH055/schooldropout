def generate_parent_message(student, language):

    sid = student["student_id"]

    if language=="English":

        return f"""
Dear Parent,

Your child (Student ID {sid}) may need additional academic support.

Please encourage regular attendance and study habits.

Thank you.
"""

    elif language=="Hindi":

        return f"""
प्रिय अभिभावक,

आपके बच्चे (Student ID {sid}) को अतिरिक्त शैक्षणिक सहायता की आवश्यकता हो सकती है।

कृपया नियमित रूप से स्कूल भेजें।

धन्यवाद।
"""

    elif language=="Tamil":

        return f"""
அன்புள்ள பெற்றோர்,

உங்கள் குழந்தை (Student ID {sid}) கூடுதல் கல்வி ஆதரவு தேவைப்படலாம்.

தயவுசெய்து பள்ளிக்கு முறையாக அனுப்பவும்.

நன்றி.
"""