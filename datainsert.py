import database


def create_bs_shelters():

    database.create_shelter('Résilience Montréal', 45.492899767755475, -73.58420220246188, '4000 Sainte-Catherine O, Westmount, QC H3Z 1P1',
                            'merde@com'
                            '', '+14388288995', '/statics/logos/Resilience.jpg')

    database.create_shelter('La Maison Benoît Labre', 45.474762190767294, -73.58785898176345, '4561 Notre-Dame St W, Montreal, Quebec H4C 1S3',
                            'merde@com', '+15149375973', '/statics/logos/Benoit.jpg')


def create_bs_shelters_info():
    database.create_shelter_info('Résilience Montréal', 0, 1, 1, 0)
    database.create_shelter_info('La Maison Benoît Labre', 1, 1, 1, 0)