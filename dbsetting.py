import pymongo
import csv


def createdatabases():
    conn = pymongo.MongoClient("localhost", 27017)
    db = conn.get_database("movies")
    db.create_collection("myMovies")
    db.create_collection("review")
    db.create_collection("users")
    db.create_collection("trailer")


def readcsv_toadd(filename , mode):
    conn = pymongo.MongoClient("localhost", 27017)
    db = conn.get_database("movies")

    with open(filename, mode, encoding="utf8") as f:
        fr = csv.DictReader(f)
        id = 1
        for row in fr:
            datadic = {"ID": id, "original_title": row['original_title'], "cast": row['cast'],
                       "director": row['director'], "overview":row['overview'],
                       "runtime": row['runtime'] ,"genres":row['genres'],
                       "release_date":row['release_date'],"release_year":row['release_year'],
                       "homepage":row['homepage'],"vote_average":(float(row['vote_average']))}
            id += 1
            #print(datadic) check
            db.myMovies.insert_one(datadic)
        print("Add to Databases")


def add_review():
    conn = pymongo.MongoClient("localhost", 27017)
    db = conn.get_database("movies")
    datadic = {"original_title":"Jurassic World", "comment":"หนังดีมากเอาคะแนนไปเลย","score":9.5, "id":"admin","nickname":"kan"}
    db.review.insert_one(datadic)

def add_trailer(filename,mode):
    conn = pymongo.MongoClient("localhost", 27017)
    db = conn.get_database("movies")
    with open(filename, mode, encoding="utf8") as f:
        fr = csv.DictReader(f)
        for row in fr:
            movie_title = str(row['title'])
            linkyou = str(row['youtubeId'])
            m = movie_title.split("(")
            dataset = {"original_title":m[0].strip(),"linkyoutube":linkyou.strip()}
            db.trailer.insert_one(dataset)




if __name__ == '__main__':
    #1.สร้างCollection
    createdatabases()
    add_review()

    #2.อ่านแล้วเพิ่มข้อมูล
    filename = "./file/tmdb_movies_data.csv"
    readcsv_toadd(filename, "r")

    filename2 = "./file/movie_youtube.csv"
    add_trailer(filename2,"r")