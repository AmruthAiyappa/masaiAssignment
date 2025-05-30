class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"User: {self.name}, Email: {self.email}")

class Instructor(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def upload_content(self):
        print(f"{self.name} uploaded content on {self.subject}.")

    def display_info(self):
        print(f"Instructor: {self.name}, Subject: {self.subject}")

class CourseCreator(Instructor):
    def __init__(self, name, email, subject):
        super().__init__(name, email, subject)
        self.courses = []

    def create_course(self, course_name):
        self.courses.append(course_name)
        print(f"Course '{course_name}' created.")

    def display_info(self):
        print(f"Course Creator: {self.name}, Courses: {', '.join(self.courses) if self.courses else 'None'}")

# Demo
creator = CourseCreator("Dr. Rao", "rao@example.com", "AI")
creator.upload_content()
creator.create_course("AI for Beginners")
creator.display_info()
