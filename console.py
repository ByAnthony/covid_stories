from models.memory import Memory
import pdb
from models.charity import Charity
from models.contributor import Contributor
from models.memory import Memory
from models.event import Event

import repositories.charity_repository as charity_repository
import repositories.contributor_repository as contributor_repository
import repositories.memory_repository as memory_repository
import repositories.event_repository as event_repository


charity_1 = Charity("NHS Charities Together", "We are the national independent charity caring for the NHS and we’re here for everyone who loves the NHS. Together with a network of over 240 NHS charities across the UK, we provide the extra support needed to care for NHS staff, patients and communities.", "https://nhscharitiestogether.co.uk")
charity_repository.save(charity_1)
charity_2 = Charity("Mind", "We provide advice and support to empower anyone experiencing a mental health problem. We campaign to improve services, raise awareness and promote understanding.", "https://www.mind.org.uk")
charity_repository.save(charity_2)
charity_3 = Charity("Shelter Scotland", "We strive every day to give people struggling with bad housing or homelessness the help they need, through our advice, support and legal services. We campaign relentlessly to achieve our vision of a safe, secure, affordable home for everyone.", "https://scotland.shelter.org.uk")
charity_repository.save(charity_3)


contributor_1 = Contributor("Eleanor", "Bailie", 27, "Teacher", "Glasgow")
contributor_repository.save(contributor_1)
contributor_2 = Contributor("Robert", "Sponge", 43, "Ecologist", "Inverness")
contributor_repository.save(contributor_2)
contributor_3 = Contributor("Laureen", "Douglas", 35, "Software Developer", "Dundee")
contributor_repository.save(contributor_3)
contributor_4 = Contributor("Bruce", "McInnes", 62, "Builder", "Lochboisdale")
contributor_repository.save(contributor_4)


memory_1 = Memory("Lorem ipsum dolor", contributor_1, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "2020-09-20", charity_2)
memory_repository.save(memory_1)

event_1 = Event("Hill Walking", "Walk for charity", charity_1, "2022-01-26")
event_repository.save(event_1)
event_2 = Event("Loch Swimming", "Swim for charity", charity_2, "2022-04-05")
event_repository.save(event_2)
event_3 = Event("Marathon", "Run for charity", charity_3, "2022-06-23")
event_repository.save(event_3)


pdb.set_trace()