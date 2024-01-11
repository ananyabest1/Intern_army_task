class Quiz:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.player_name = ""
        self.reg_no = ""
        self.age = ""
        self.total_score = 0

    def get_player_info(self):
        self.player_name = input("Enter your name: ")
        self.reg_no = input("Enter your registration number: ")
        self.age = input("Enter your age: ")

    def multiple_choice_question(self, question, options, correct_option):
        self.questions.append({
            'question': question,
            'options': options,
            'correct_option': correct_option
        })

    def true_false_question(self, question, correct_answer):
        self.questions.append({
            'question': question,
            'correct_answer': correct_answer
        })

    def conduct_quiz(self):
        self.get_player_info()

        for index, question_data in enumerate(self.questions, start=1):
            print(f"\nQuestion {index}: {question_data['question']}")
            if 'options' in question_data:  # Multiple-choice question
                for i, option in enumerate(question_data['options'], start=1):
                    print(f"{i}. {option}")

                user_answer = int(input("Enter your choice (1, 2, 3, etc.): "))
                correct_option = question_data['correct_option']
                if user_answer == correct_option:
                    self.answers.append(True)
                    self.total_score += 1
                    print("Correct!\n")
                else:
                    self.answers.append(False)
                    print(f"Wrong! Correct answer is {question_data['options'][correct_option - 1]}\n")

            elif 'correct_answer' in question_data:  # True/False question
                user_answer = input("Enter True or False: ").lower()
                correct_answer = str(question_data['correct_answer']).lower()
                if user_answer == correct_answer:
                    self.answers.append(True)
                    self.total_score += 1
                    print("Correct!\n")
                else:
                    self.answers.append(False)
                    print(f"Wrong! Correct answer is {question_data['correct_answer']}\n")

        self.display_results()

    def display_results(self):
        print("\nQuiz Results:")
        print(f"Player Name: {self.player_name}")
        print(f"Registration Number: {self.reg_no}")
        print(f"Age: {self.age}\n")

        for index, (question_data, answer) in enumerate(zip(self.questions, self.answers), start=1):
            print(f"Question {index}: {question_data['question']}")
            if 'options' in question_data:
                print(f"Your Answer: {question_data['options'][answer - 1]}")
                print(f"Correct Answer: {question_data['options'][question_data['correct_option'] - 1]}")
            elif 'correct_answer' in question_data:
                print(f"Your Answer: {answer}")
                print(f"Correct Answer: {question_data['correct_answer']}")

            print()

        print(f"Total Score: {self.total_score}/{len(self.questions)}")
        print("Thanks for playing!")

if __name__ == "__main__":
    quiz = Quiz()

    # Adding multiple-choice questions
    quiz.multiple_choice_question("Who developed Python Programming Language?", [" Wick van Rossum", "Berlin", "Guido van Rossum", "Madrid"], 3)
    quiz.multiple_choice_question("Which programming language is this quiz written in?", ["Python", "Java", "C++", "JavaScript"], 4)
    quiz.multiple_choice_question("Which type of Programming does Python support?", ["object-oriented programming", " structured programming", "functional programming", "all of the mentioned"], 4)
    quiz.multiple_choice_question("Is Python case sensitive when dealing with identifiers?", ["yes", " structured programming", "functional programming", "all of the mentioned"], 1)
    quiz.multiple_choice_question("Which of the following is the correct extension of the Python file?", ["object-oriented programming", " structured programming", ".py", "all of the mentioned"], 3)

    # Adding true/false questions
    quiz.true_false_question("Python is a compiled language.", False)
    quiz.true_false_question("The Earth is flat.", False)

    # Conducting the quiz
    quiz.conduct_quiz()
