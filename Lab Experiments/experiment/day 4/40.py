
# Recommendation System using Collaborative Filtering

# User movie ratings
ratings = {
    'User1': {
        'Movie A': 5,
        'Movie B': 4,
        'Movie C': 0,
        'Movie D': 0
    },
    'User2': {
        'Movie A': 4,
        'Movie B': 5,
        'Movie C': 3,
        'Movie D': 0
    },
    'User3': {
        'Movie A': 0,
        'Movie B': 0,
        'Movie C': 5,
        'Movie D': 4
    },
    'User4': {
        'Movie A': 5,
        'Movie B': 4,
        'Movie C': 4,
        'Movie D': 5
    }
}

# Calculate similarity between two users
def similarity(user1, user2):

    common_movies = []

    for movie in ratings[user1]:
        if ratings[user1][movie] > 0 and ratings[user2][movie] > 0:
            common_movies.append(movie)

    if not common_movies:
        return 0

    sum1 = 0
    sum2 = 0

    for movie in common_movies:
        sum1 += ratings[user1][movie] * ratings[user2][movie]
        sum2 += ratings[user1][movie] ** 2
        sum2 += ratings[user2][movie] ** 2

    import math

    return sum1 / (
        math.sqrt(
            sum(ratings[user1][m] ** 2 for m in common_movies)
            * sum(ratings[user2][m] ** 2 for m in common_movies)
        )
    )


# Recommend movies
def recommend(target_user):

    scores = {}

    for other_user in ratings:

        if other_user == target_user:
            continue

        sim = similarity(target_user, other_user)

        for movie, rating in ratings[other_user].items():

            if ratings[target_user][movie] == 0 and rating > 0:

                if movie not in scores:
                    scores[movie] = 0

                scores[movie] += sim * rating

    recommendations = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations


# Main program
print("===== MOVIE RECOMMENDATION SYSTEM =====")

user = input("Enter user name (User1/User2/User3/User4): ")

if user in ratings:

    print("\nRecommendations for", user)

    result = recommend(user)

    if result:
        for movie, score in result:
            print(movie, "Recommendation Score:", round(score, 2))
    else:
        print("No recommendations available.")

else:
    print("Invalid User Name!")
