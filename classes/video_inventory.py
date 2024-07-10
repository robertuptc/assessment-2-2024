import csv


class VideoInventory:

    @classmethod
    def load_inventory(cls):
        all_movies = []
        with open('data/inventory.csv', newline='') as csvfile:
            file_reader = csv.DictReader(csvfile)
            for row in file_reader:
                movie = cls(**row)
                all_movies.append(movie)
        return all_movies


    def __init__(self, id, title, rating, release_year, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available
    
    def __repr__(self):
        return f"{self.id} | {self.title} | {self.rating} | {self.release_year} | {self.copies_available}"