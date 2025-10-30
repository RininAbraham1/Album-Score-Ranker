import requests

# Mock data for testing / fallback
sample_albums = [
    {"title": "To Pimp a Butterfly", "artist": "Kendrick Lamar", "score": 95},
    {"title": "Songs in the Key of Life", "artist": "Stevie Wonder", "score": 94},
    {"title": "good kid, m.A.A.d city", "artist": "Kendrick Lamar", "score": 94},
    {"title": "Wish You Were Here", "artist": "Pink Floyd", "score": 94},
    {"title": "In Rainbows", "artist": "Radiohead", "score": 93},
    {"title": "Lift Your Skinny Fists Like Antennas to Heaven", "artist": "Godspeed You Black Emperor!", "score": 93},
    {"title": "OK Computer", "artist": "Radiohead", "score": 93},
    {"title": "Vespertine", "artist": "Björk", "score": 93},
    {"title": "Illmatic", "artist": "Nas", "score": 93},
    {"title": "Madvillainy", "artist": "Madvillain", "score": 93},
    {"title": "What's Going On", "artist": "Marvin Gaye", "score": 92},
    {"title": "Grace", "artist": "Jeff Buckley", "score": 92},
    {"title": "Abbey Road", "artist": "The Beatles", "score": 92},
    {"title": "The Black Saint and the Sinner Lady", "artist": "Mingus", "score": 92},
    {"title": "Enter the Wu-Tang (36 Chambers)", "artist": "Wu-Tang Clan", "score": 92},
    {"title": "In the Court of the Crimson King", "artist": "King Crimson", "score": 92},
    {"title": "The Rise and Fall of Ziggy Stardust and the Spiders from Mars", "artist": "David Bowie", "score": 91},
    {"title": "Homogenic", "artist": "Björk", "score": 91},
    {"title": "Deathconsciousness", "artist": "Have a Nice Life", "score": 91},
    {"title": "The Glow Pt. 2", "artist": "The Microphones", "score": 91},
    {"title": "The Miseducation of Lauryn Hill", "artist": "Lauryn Hill", "score": 91},
    {"title": "The Dark Side of the Moon", "artist": "Pink Floyd", "score": 91},
    {"title": "Kid A", "artist": "Radiohead", "score": 91},
    {"title": "When the Pawn...", "artist": "Fiona Apple", "score": 91},
    {"title": "Toxicity", "artist": "System of a Down", "score": 91},
    {"title": "Electric Ladyland", "artist": "The Jimi Hendrix Experience", "score": 91},
    {"title": "Purple Rain", "artist": "Prince and The Revolution", "score": 91},
    {"title": "Discovery", "artist": "Daft Punk", "score": 91},
    {"title": "Illinois", "artist": "Sufjan Stevens", "score": 91},
    {"title": "The College Dropout", "artist": "Kanye West", "score": 91},
    {"title": "Love Deluxe", "artist": "Sade", "score": 91},
    {"title": "Animals", "artist": "Pink Floyd", "score": 91},
    {"title": "Kind of Blue", "artist": "Miles Davis", "score": 91},
    {"title": "Disintegration", "artist": "The Cure", "score": 91},
    {"title": "IGOR", "artist": "Tyler, The Creator", "score": 91},
    {"title": "The Low End Theory", "artist": "A Tribe Called Quest", "score": 90},
    {"title": "Ants From Up There", "artist": "Black Country, New Road", "score": 90},
    {"title": "LONG SEASON", "artist": "Fishmans", "score": 90},
    {"title": "The Infamous", "artist": "Mobb Deep", "score": 90},
    {"title": "A Love Supreme", "artist": "John Coltrane", "score": 90},
    {"title": "Clube da Esquina", "artist": "Milton Nascimento & Lô Borges", "score": 90},
    {"title": "Slow Riot for New Zerø Kanada E.P.", "artist": "Godspeed You Black Emperor!", "score": 90},
    {"title": "Atrocity Exhibition", "artist": "Danny Brown", "score": 90},
    {"title": "Imaginal Disk", "artist": "Magdalena Bay", "score": 90},
    {"title": "Aquemini", "artist": "OutKast", "score": 90},
    {"title": "Thriller", "artist": "Michael Jackson", "score": 90},
    {"title": "LP! (Offline Version)", "artist": "JPEGMAFIA", "score": 90},
    {"title": "Black on Both Sides", "artist": "Mos Def", "score": 90},
    {"title": "Bitches Brew", "artist": "Miles Davis", "score": 90},
    {"title": "Dummy", "artist": "Portishead", "score": 90}
]

def fetch_album_data(api_mode=False):
    """
    Fetch albums from either the mock data or an API (Spotify, MusicBrainz, etc.).
    Set api_mode=True to fetch from a real API.
    """
    if api_mode:
        try:
            # Example using Spotify API (requires API key/token)
            headers = {"Authorization": "Bearer BQBFz03X2GVHi2_7AXW86NeTdtLXZjuKw0B930ZM3EZclztArbNOAV52bsZ98abio_Sq-N6AwMo-MLtL-hD7X79Ij4Nc__y6Ngo_5FAFhF1R7SkhkyTB_XeF2cEqmko2TLTqKvALu2w"}

            url = "https://api.spotify.com/v1/playlists/37i9dQZF1DXcBWIGoYBM5M/tracks"  # Top 50 tracks playlist example
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            albums = []
            for item in data['items']:
                album_info = item['track']['album']
                albums.append({
                    "title": album_info['name'],
                    "artist": ", ".join([artist['name'] for artist in album_info['artists']]),
                    "score": 90  # default since API won't have user score
                })
            return albums
        except Exception as e:
            print("API fetch failed, falling back to mock data:", e)
            return sample_albums
    else:
        return sample_albums

if __name__ == "__main__":
    albums = fetch_album_data(api_mode=True)
    for a in albums:
        print(f"{a['title']} - {a['artist']} ({a['score']})")
