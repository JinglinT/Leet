class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        def normalize(email):
            local, domain = email.split('@')

            local = local.split('+')[0].replace('.', '')

            return (local, domain)

        uniques = set()

        for email in emails:
            uniques.add(normalize(email))

        return len(uniques)
