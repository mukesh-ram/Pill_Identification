# pill_dictionary.py

class PillDictionary:
    def __init__(self):
        self.pill_info = {
            'Aceclofenac, Paracetamol & Serratiopeptidase': {
                'benefits': 'Benefit information for Aceclofenac, Paracetamol & Serratiopeptidase.',
                'usage': 'Usage information for Aceclofenac, Paracetamol & Serratiopeptidase.',
                'tablets': ['Aceclospa', 'Paraserr', 'Zerodol-SP']
            },
            'Itraconazole': {
                'benefits': 'Benefit information for Itraconazole.',
                'usage': 'Usage information for Itraconazole.',
                'tablets': ['Itrasys', 'Canditral', 'Itrazol']
            },
            'Montelukast Sodium & Levocetirizine Hydrochloride': {
                'benefits': 'Benefit information for Montelukast Sodium & Levocetirizine Hydrochloride.',
                'usage': 'Usage information for Montelukast Sodium & Levocetirizine Hydrochloride.',
                'tablets': ['Montair-LC', 'Levocet-M', 'Montecip-LC']
            },
            'Paracetamol': {
                'benefits': 'Benefit information for Paracetamol.',
                'usage': 'Usage information for Paracetamol.',
                'tablets': ['Crocin', 'Calpol', 'Dolo-650']
            }
        }

    def get_pill_info(self, pill_name):
        return self.pill_info.get(pill_name, {'benefits': 'Not available', 'usage': 'Not available', 'tablets': []})
