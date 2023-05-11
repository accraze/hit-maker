from rich.console import Console
from rich.table import Table

from service import generate_band_name_and_hit_single

console = Console()


def display_data(data):
    console.print(data)


if __name__ == "__main__":
    artists = console.input("Enter similar artistic influences: ")
    song_data = generate_band_name_and_hit_single(artists)
    display_data(song_data)
