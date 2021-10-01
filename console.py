from models.memory import Memory
import pdb
from models.charity import Charity
from models.contributor import Contributor
from models.memory import Memory
from models.event import Event
from models.ticket import Ticket

import repositories.charity_repository as charity_repository
import repositories.contributor_repository as contributor_repository
import repositories.memory_repository as memory_repository
import repositories.event_repository as event_repository
import repositories.ticket_repository as ticket_repository


charity_1 = Charity("NHS Charities Together", "We are the national independent charity caring for the NHS and we’re here for everyone who loves the NHS. Together with a network of over 240 NHS charities across the UK, we provide the extra support needed to care for NHS staff, patients and communities.", "https://nhscharitiestogether.co.uk")
charity_repository.save(charity_1)
charity_2 = Charity("Mind", "We provide advice and support to empower anyone experiencing a mental health problem. We campaign to improve services, raise awareness and promote understanding.", "https://www.mind.org.uk")
charity_repository.save(charity_2)
charity_3 = Charity("Shelter Scotland", "We strive every day to give people struggling with bad housing or homelessness the help they need, through our advice, support and legal services. We campaign relentlessly to achieve our vision of a safe, secure, affordable home for everyone.", "https://scotland.shelter.org.uk")
charity_repository.save(charity_3)
charity_4 = Charity("Age Scotland", "Age Scotland is the national charity for older people. We work to improve the lives of everyone over the age of 50 so that they can love later life.", "https://www.ageuk.org.uk/scotland/")
charity_repository.save(charity_4)


contributor_1 = Contributor("Eleanor", "Bailie", 27, "Teacher", "Glasgow")
contributor_repository.save(contributor_1)
contributor_2 = Contributor("Robert", "Sponge", 43, "Ecologist", "Inverness")
contributor_repository.save(contributor_2)
contributor_3 = Contributor("Laureen", "Douglas", 35, "Software Developer", "Dundee")
contributor_repository.save(contributor_3)
contributor_4 = Contributor("Bruce", "MacInnes", 62, "Builder", "Lochboisdale")
contributor_repository.save(contributor_4)
contributor_5 = Contributor("John", "Rennie", 55, "Councellor", "Stirling")
contributor_repository.save(contributor_5)


memory_1 = Memory("Lorem ipsum dolor", contributor_1, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "2020-09-27", charity_2)
memory_repository.save(memory_1)
memory_2 = Memory("Lorem ipsum dolor", contributor_2, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "2020-01-26", charity_4)
memory_repository.save(memory_2)
memory_3 = Memory("Lorem ipsum dolor", contributor_3, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "2020-06-23", charity_1)
memory_repository.save(memory_3)
memory_4 = Memory("Lorem ipsum dolor", contributor_4, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "2020-05-04", charity_3)
memory_repository.save(memory_4)
memory_5 = Memory("Lorem ipsum dolor", contributor_5, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "2020-12-18", charity_1)
memory_repository.save(memory_5)
memory_6 = Memory("Lorem ipsum dolor", contributor_1, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "2021-02-28", charity_2)
memory_repository.save(memory_6)
memory_7 = Memory("Lorem ipsum dolor", contributor_2, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "2020-07-17", charity_3)
memory_repository.save(memory_7)
memory_8 = Memory("Lorem ipsum dolor", contributor_3, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "2021-04-14", charity_4)
memory_repository.save(memory_8)
memory_9 = Memory("Lorem ipsum dolor", contributor_4, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "2021-09-30", charity_1)
memory_repository.save(memory_9)
memory_10 = Memory("Lorem ipsum dolor", contributor_5, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "2020-08-15", charity_2)
memory_repository.save(memory_10)

event_1 = Event("Hill walking", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", charity_1, "2022-01-26")
event_repository.save(event_1)
event_2 = Event("Loch swimming", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", charity_2, "2022-04-05")
event_repository.save(event_2)
event_3 = Event("Marathon", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", charity_3, "2022-06-23")
event_repository.save(event_3)
event_4 = Event("Exhibition", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", charity_4, "2022-09-27")
event_repository.save(event_4)
event_5 = Event("Cycling race", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", charity_1, "2022-04-17")
event_repository.save(event_5)
event_6 = Event("Symposium", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", charity_2, "2022-10-23")
event_repository.save(event_6)
event_7 = Event("Sailing", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", charity_3, "2022-06-06")
event_repository.save(event_7)
event_8 = Event("Castle visit", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", charity_4, "2022-04-22")
event_repository.save(event_8)
event_9 = Event("Wine testing", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", charity_2, "2022-11-15")
event_repository.save(event_9)
event_10 = Event("Restaurant", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", charity_4, "2022-12-12")
event_repository.save(event_10)

ticket_1 = Ticket(event_1, contributor_1)
ticket_repository.save(ticket_1)
ticket_2 = Ticket(event_2, contributor_2)
ticket_repository.save(ticket_2)
ticket_3 = Ticket(event_3, contributor_3)
ticket_repository.save(ticket_3)
ticket_4 = Ticket(event_4, contributor_4)
ticket_repository.save(ticket_4)
ticket_5 = Ticket(event_5, contributor_1)
ticket_repository.save(ticket_5)
ticket_6 = Ticket(event_6, contributor_3)
ticket_repository.save(ticket_6)
ticket_7 = Ticket(event_7, contributor_1)
ticket_repository.save(ticket_7)


pdb.set_trace()