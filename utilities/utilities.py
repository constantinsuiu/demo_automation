

class Utilities:

    def move_up_directory(self, current_path, nr_of_moves):
        print(current_path)
        return "/".join(current_path.split("/")[:0-nr_of_moves])