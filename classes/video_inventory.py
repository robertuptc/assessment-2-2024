import csv


class VideoInventory:
    all_movies = []

    @classmethod
    def load_inventory(cls):
        # all_movies = []
        with open('data/inventory.csv', newline='') as csvfile:
            file_reader = csv.DictReader(csvfile)
            for row in file_reader:
                movie = cls(**row)
                cls.all_movies.append(movie)
        return cls.all_movies


    @classmethod
    def rent_movie(cls, rental, current_copies):
        for movie in cls.all_movies:
            if (movie.title).lower() == rental:
                movie.copies_available = int(movie.copies_available) - 1
        with open('data/inventory.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'rating', 'release_year', 'copies_available']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for movie in cls.all_movies:
                writer.writerow({
                    'id': movie.id, 
                    'title': movie.title, 
                    'rating': movie.rating, 
                    'release_year': movie.release_year,
                    'copies_available': movie.copies_available
                })

    @classmethod
    def return_video(cls):
        with open('data/inventory.csv', 'w', newline='') as csvfile:
            fieldnames = fieldnames = ['id', 'title', 'rating', 'release_year', 'copies_available']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for movie in cls.all_movies:
                writer.writerow({
                    'id': movie.id, 
                    'title': movie.title, 
                    'rating': movie.rating, 
                    'release_year': movie.release_year,
                    'copies_available': movie.copies_available
                })


    def __init__(self, id, title, rating, release_year, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available
    
    def __repr__(self):
        return f"{self.id} | {self.title} | {self.rating} | {self.release_year} | {self.copies_available}"