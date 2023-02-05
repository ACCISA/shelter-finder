import database


def create_bs_shelters():
    database.create_shelter('Résilience Montréal', 45.492899767755475, -73.58420220246188,
                            '4000+Sainte-Catherine+O+Westmount+QC+H3Z+1P1',
                            'truc@com', '+14388288995', '/static/logos/Resilience.jpg')

    database.create_shelter('La Maison Benoît Labre', 45.474762190767294, -73.58785898176345,
                            '4561+Notre-Dame+St+W+Montreal+Quebec+H4C+1S3',
                            'truc@com', '+15149375973', '/static/logos/Benoit.jpg')

    database.create_shelter('La Maison des Femmes', 45.474762190767294, -73.58785898176345,
                            '6767+Chem+de+la+Côte+des+Neiges+#597+Montréal+QC+H3S+2T6',
                            'truc@com', '+15147359027', '/static/logos/femmes.jpg')

    database.create_shelter('La Porte Ouverte', 45.51269980060793, -73.57470560878401,
                            '3535+Av+du+Parc+Montréal+QC+H2X+2H8',
                            'truc@com', '+15149391970', '/static/logos/porte.jpg')


def create_bs_shelters_info():
    database.create_shelter_info('Résilience Montréal', 0, 1, 1, 0)
    database.create_shelter_info('La Maison Benoît Labre', 1, 1, 1, 0)
    database.create_shelter_info('La Maison des Femmes', 1, 0, 1, 0)
    database.create_shelter_info('La Porte Ouverte', 0, 0, 1, 0)
