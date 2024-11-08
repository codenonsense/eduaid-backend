from fastapi import APIRouter, HTTPException


summaries_router = APIRouter()

@summaries_router.get('/summaries')
async def get_summaries(link):
    print(link)
    summaries = [
    {
        "title": "Physics - Basic Introduction",
        "link": "http://www.youtube.com/watch?v=b1t41Q3xRM8",
        "summary": "Introduces fundamental physics concepts like distance, displacement, speed, velocity, acceleration, and Newton's laws of motion."
    },
    {
        "title": "ALL OF PHYSICS explained in 14 Minutes",
        "link": "http://www.youtube.com/watch?v=ZAqIoDhornk",
        "summary": "Provides a comprehensive overview of physics, covering classical mechanics, electromagnetism, quantum mechanics, and relativity."
    },
    {
        "title": "Physics for Beginners (Ep-1) | Motion | Basic Physics",
        "link": "http://www.youtube.com/watch?v=wUgYa5YLBbM",
        "summary": "Explains concepts of motion, speed, velocity, acceleration, and force."
    },
    {
        "title": "01 - Introduction to Physics, Part 1 (Force, Motion & Energy) - Online Physics Course",
        "link": "http://www.youtube.com/watch?v=i_CijGuk7fw",
        "summary": "Introduces physics, its importance, main topics, and problem-solving techniques."
    },
    {
        "title": "Introduction to physics | One-dimensional motion | Physics | Khan Academy",
        "link": "http://www.youtube.com/watch?v=uIojjqSm0m4",
        "summary": "Discusses fundamental questions in physics and its role as a foundational science."
    },
    {
        "title": "All of Physics Summarized in 7 Minutes",
        "link": "http://www.youtube.com/watch?v=T3aDOerjgJ8",
        "summary": "Provides a concise overview of core physics concepts and theories."
    },
    {
        "title": "All of AQA Energy explained in 7 minutes - GCSE Physics 9-1 REVISION",
        "link": "http://www.youtube.com/watch?v=UyeFNz7sHYg",
        "summary": "Covers energy in physics, including various forms of energy and energy transfer."
    },
    {
        "title": "Chemistry explained in 5 minutes",
        "link": "http://www.youtube.com/watch?v=pyVO0gzYWzk",
        "summary": "Uses the analogy of Lego bricks to explain atoms and molecules."
    },
    {
        "title": "GENERAL CHEMISTRY explained in 19 Minutes",
        "link": "http://www.youtube.com/watch?v=5iTOphGnCtg",
        "summary": "Provides a comprehensive overview of general chemistry, covering atoms, elements, the periodic table, chemical bonding, and chemical reactions."
    },
    {
        "title": "GENERAL CHEMISTRY EXPLAINED IN 5 MINUTES | MY PAINT EXPLAINER",
        "link": "http://www.youtube.com/watch?v=vgRjacM6cys",
        "summary": "Offers a concise overview of fundamental chemistry concepts."
    },
    {
        "title": "Atom Explained in Simple Terms",
        "link": "http://www.youtube.com/watch?v=ajg07Dnc1BQ",
        "summary": "Covers the basic structure of atoms, including protons, neutrons, and electrons."
    },
    {
        "title": "The Magic of Chemistry Explained in 5 Minutes!",
        "link": "http://www.youtube.com/watch?v=y0G7y0-MKWs",
        "summary": "Introduces chemistry and the concept of chemical reactions."
    },
    {
        "title": "Introduction to chemistry | Atoms, compounds, and ions | Chemistry | Khan Academy",
        "link": "http://www.youtube.com/watch?v=Rd4a1X3B61w",
        "summary": "Explains chemistry, the composition of matter, and chemical bonding."
    },
    {
        "title": "The Entire AP Chemistry Course in 19 Minutes | Speed Review for AP Chem",
        "link": "http://www.youtube.com/watch?v=o4myTMguET4",
        "summary": "Provides a comprehensive review of the AP Chemistry course."
    },
    {
        "title": "Python Tutorial for Absolute Beginners | 1 - Install Python",
        "link": "http://www.youtube.com/watch?v=pyVO0gzYWzk2",
        "summary": "Covers installation of Python."
    },
    {
        "title": "Python Tutorial for Absolute Beginners | 2 - What is Python ?",
        "link": "http://www.youtube.com/watch?v=pyVO0gzYWzk3",
        "summary": "Introduces Python."
    },
    {
        "title": "Python Tutorial for Absolute Beginners | 3 - First Python Program",
        "link": "http://www.youtube.com/watch?v=pyVO0gzYWzk4",
        "summary": "Guides you through creating your first Python program."
    },
    {
        "title": "Python Tutorial for Absolute Beginners | 4 - Taking Input from User",
        "link": "http://www.youtube.com/watch?v=pyVO0gzYWzk5",
        "summary": "Explains how to take input from the user in Python."
    },
    {
        "title": "Python Tutorial for Absolute Beginners | 5 - Operators in Python",
        "link": "http://www.youtube.com/watch?v=pyVO0gzYWzk6",
        "summary": "Covers operators in Python."
    },
    {
        "title": "Python Tutorial for Absolute Beginners | 6 - Strings in Python",
        "link": "http://www.youtube.com/watch?v=pyVO0gzYWzk7",
        "summary": "Discusses strings in Python."
    },
    {
        "title": "Python Tutorial for Absolute Beginners | 7 - Lists in Python",
        "link": "http://www.youtube.com/watch?v=pyVO0gzYWzk8",
        "summary": "Covers lists in Python."
    }
]
    matching_summary = [summary for summary in summaries if summary["link"] == link]
    print(matching_summary)
    
    raise HTTPException(status_code=200, detail=f"{matching_summary}")
