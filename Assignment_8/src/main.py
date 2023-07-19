from src.domain.person import Person
from src.repository.activityRepo import ActivityRepo
from src.repository.personRepo import PersonRepo
from src.services.services import Services
from src.ui.user_interface import User_Interface

if __name__ == "__main__":
    personsRepo = PersonRepo()

    activitiesRepo = ActivityRepo()

    services = Services(personsRepo, activitiesRepo)

    user_interface = User_Interface(services)


    user_interface()
