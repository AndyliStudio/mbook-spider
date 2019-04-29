import pymongo
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
import logging


class MongoDBConnect():

    def __init__(self):
        url = ''
        settings = get_project_settings()
        if settings['MONGO_AUTH']:
            url = "mongodb://{username}:{password}@{host}:{port}/{db_name}?authMechanism=MONGODB-CR".format(
                username=settings['MONGODB_USER'], password=settings['MONGODB_PASS'], host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'], db_name=settings['MONGODB_DB'])
        else:
            url = "mongodb://{host}:{port}/{db_name}".format(
                host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'], db_name=settings['MONGODB_DB'])

        logging.info('MongoDB连接地址：%s', url)

        try:
            connection = pymongo.MongoClient(url)
            db = connection[settings['MONGODB_DB']]
            self.Book = db['books']
            self.Chapter = db['chapters']
        except pymongo.errors.ConnectionFailure as e:
            logging.error('MongoDB连接失败：%s', e)


if __name__ == '__main__':
    connect = MongoDBConnect()
