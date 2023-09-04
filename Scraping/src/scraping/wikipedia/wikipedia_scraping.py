
import wikipedia


def scraping(entity: str):
    entity_summary = wikipedia.summary(entity)
    print(entity_summary)


def main():
    try:
        scraping("Bosch afafafa")
    except wikipedia.exceptions.PageError as e:
        print(e)


if __name__ == "__main__":
    main()
