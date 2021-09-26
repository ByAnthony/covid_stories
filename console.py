from models.memory import Memory
import pdb
from models.charity import Charity
from models.contributor import Contributor
from models.memory import Memory

import repositories.charity_repository as charity_repository
import repositories.contributor_repository as contributor_repository
import repositories.memory_repository as memory_repository


charity_1 = Charity("NHS Charities Together", "we provide the extra support needed to care for NHS staff, patients and communities", "https://nhscharitiestogether.co.uk")
charity_repository.save(charity_1)
charity_2 = Charity("Mind", "We provide advice and support to empower anyone experiencing a mental health problem", "https://www.mind.org.uk")
charity_repository.save(charity_2)
charity_3 = Charity("Shelter Scotland", "We strive every day to give people struggling with bad housing or homelessness the help they need", "https://scotland.shelter.org.uk")
charity_repository.save(charity_3)


contributor_1 = Contributor("Eleanor", "Bailie", 27, "Teacher", "Glasgow")
contributor_repository.save(contributor_1)
contributor_2 = Contributor("Robert", "Sponge", 43, "Ecologist", "Inverness")
contributor_repository.save(contributor_2)
contributor_3 = Contributor("Laureen", "Douglas", 35, "Software Developer", "Dundee")
contributor_repository.save(contributor_3)
contributor_4 = Contributor("Bruce", "McInnes", 62, "Builder", "Lochboisdale")
contributor_repository.save(contributor_4)


memory_1 = Memory("Lacking Nature", contributor_1, "My Story of lockdown", "2020-09-20", charity_2)
memory_repository.save(memory_1)


pdb.set_trace()