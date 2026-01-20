import sys


def main():
    print("=== Player Score Analytics ===")
    argc = len(sys.argv)
    argv = sys.argv
    if argc <= 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    scores = []
    for i in range(1, argc):
        try:
            value = int(argv[i])
        except ValueError:
            print(f"Invalid score: {argv[i]} its not a valid number.")
            return
        scores += [value]

    print(f"Scores processed: {scores}")
    print("Total players", len(scores))
    print("Total score:", sum(scores))
    print("Average score:", sum(scores) / len(scores))
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:", max(scores) - min(scores))


if __name__ == "__main__":
    main()
