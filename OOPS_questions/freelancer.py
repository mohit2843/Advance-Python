# #freelancer marketplace simulation
# #register freelancer and client, assigned project and process paymennts.
class Freelancer:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.projects = []
        self.earnings = 0

    def add_project(self, project):
        self.projects.append(project)

    def complete_project(self, project):
        if project in self.projects:
            self.earnings += project.payment
            self.projects.remove(project)
            print(f"{self.name} completed '{project.title}' and earned ${project.payment}")
        else:
            print(f"{self.name} is not assigned to '{project.title}'")


class Client:
    def __init__(self, name):
        self.name = name
        self.projects = []

    def post_project(self, title, payment):
        project = Project(title, payment)
        self.projects.append(project)
        print(f"{self.name} posted project '{title}' with payment ${payment}")
        return project


class Project:
    def __init__(self, title, payment):
        self.title = title
        self.payment = payment
        self.assigned_freelancer = None

    def assign_freelancer(self, freelancer):
        self.assigned_freelancer = freelancer
        freelancer.add_project(self)
        print(f"Project '{self.title}' assigned to {freelancer.name}")

freelancers = []
clients = []

n = int(input("Enter number of users to register: "))

for _ in range(n):
    name = input("Enter name: ")
    role = input("Enter role (freelancer/client): ").lower()

    if role == "freelancer":
        skills = input("Enter skills (comma separated): ").split(",")
        skills = [s.strip() for s in skills]
        freelancers.append(Freelancer(name, skills))

    elif role == "client":
        clients.append(Client(name))

    else:
        print("Invalid role")

for client in clients:
    title = input(f"\n{client.name}, enter project title: ")
    payment = float(input("Enter project payment: "))

    project = client.post_project(title, payment)

    freelancer_name = input("Enter freelancer name to assign: ")

    freelancer = None
    for f in freelancers:
        if f.name.lower() == freelancer_name.lower():
            freelancer = f
            break

    if freelancer:
        project.assign_freelancer(freelancer)

        complete = input("Mark project as completed? (yes/no): ").lower()
        if complete == "yes":
            freelancer.complete_project(project)
    else:
        print("Freelancer not found")

print("\n--- Freelancer Earnings ---")
for f in freelancers:
    print(f"{f.name}: ${f.earnings}")            