from django.shortcuts import render # type: ignore

def resume_view(request):
    resume_data = {
        'name': 'Akshayaa Prabakar',
        'location': 'New York, USA',
        'phone': '+1 1234567890',
        'email': '123@gmail.com',
        'linkedin': 'https://www.linkedin.com/in/akshayaa-prabakar-7b1979282/',
        'education': [
            {'degree': 'M.S. in Computer Science', 'school': 'New York University', 'years': '2024 - 2026'},
            {'degree': 'B.E. in Computer Science & Engineering', 'school': 'Anna University', 'years': '2018 - 2022'}
        ],
        'skills': [
            'Python', 'SQL', 'ETL', 'Snowflake', 'Informatica PowerCenter', 'Teradata', 
            'Ab Initio', 'PySpark', 'Apache Kafka', 'MongoDB', 'Control-M', 'JIRA', 
            'Git', 'Tableau', 'Unix', 'Hadoop'
        ],
        'projects': [
            {'title': 'SLIQ - Scalable Classifier', 'description': 'Built a fast and scalable classifier for data mining using Python.'},
            {'title': 'BOHB on MNIST', 'description': 'Implemented MNIST handwritten digit classification using deep learning.'},
            {'title': 'Generator Health Monitoring', 'description': 'Developed an ML-based real-time monitoring system for generator health.'}
        ],
        'experience': [
            {
                'company': 'Accenture Solutions Private Limited',
                'position': 'Data Engineering Associate',
                'duration': '10/2022 – 07/2024',
                'responsibilities': [
                    "Optimized data transformation processes with Ab Initio and Informatica PowerCenter, increasing data accuracy by 25%.",
                    "Developed and optimized Control-M jobs, streamlining ETL workflows and minimizing errors.",
                    "Designed, developed, and optimized stored procedures, views, and tables using Teradata and Snowflake.",
                    "Conducted comprehensive data validation, migration, analysis, and testing to maintain high data integrity.",
                    "Managed change-related activities, including Change Tasks (Ctasks) and Routine Tasks (Rtasks), implementing new features and processes.",
                    "Utilized advanced query techniques with Teradata to analyze data patterns, enhancing ETL performance by 30% over a 6-month period."
                ],
            }
        ],
        'certifications': [
            'SC-900: Microsoft Security, Compliance and Identity Fundamentals',
            'AZ-500: Microsoft Azure Security Technologies',
            'DP-203: Data Engineering on Microsoft Azure'
        ]
    }
    return render(request, 'cv_app/resume.html', resume_data)
