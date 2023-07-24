import random

class Company():
    def __init__(self):
        self.company_name = self.generateCompanyName()
        self.company_staff = self.generateCompanyStaff()

    def generateCompanyName(self):
        # List of prefixes
        prefixes = [
        "Sunrise",
        "Moonlight",
        "Starlight",
        "Golden",
        "Silver",
        "Crystal",
        "Emerald",
        "Ocean",
        "Harmony",
        "Rainbow",
        "Enchanted",
        "Mystic",
        "Serenity",
        "Evergreen",
        "Aurora",
        "Whisper",
        "Petal",
        "Cascade",
        "Eagle",
        "Horizon"
        ]

        # List of suffixes
        suffixes = [
        "Solutions",
        "Enterprises",
        "Group",
        "Inc",
        "Innovations",
        "Corp",
        "Technologies",
        "Global",
        "Ventures",
        "Systems",
        "Worldwide",
        "Partners",
        "Industries",
        "Network",
        "Services",
        "Digital",
        "Tech",
        "Consulting",
        "TechCorp",
        "Enterprize",
        ]

        prefix = random.choice(prefixes)
        suffix = random.choice(suffixes)

        return f"{prefix} {suffix}"

    def generateCompanyStaff(self):
        num = random.randrange(1, 999,99)
        return num
