from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, args):
        status = args.get('status')
        page = args.get('page')

        if status is not None and status == 'new':
            return self.dao.get_all_newest()
        if page is not None:
            return self.dao.get_all_by_page((page-1)*12)
        else:
            return self.dao.get_all()
