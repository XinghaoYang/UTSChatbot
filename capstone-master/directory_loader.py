import csv
import textwrap
from difflib import get_close_matches

type_dict = {
    'stm' : 'Stream',
    'maj' : 'Major',
    'smj' : 'Sub-major',
    'cbk' : 'Choice Block',
    '' : 'Subject',
    'c' : 'Course'
}

cp_length = 3
id_length = 8

default_cpath = 'data/courses.csv'
default_rpath = 'data/relations.csv'
default_ipath = 'data/items.csv'
default_npath = 'data/alt_names.csv'


def extract_digits(key):
    return ''.join(k for k in key if k.isdigit())


class Directory:
    class Substructure:
        def __init__(self, item_id, name, item_type, cp, year_10143,
                     year_09019, year_10148_BISM, year_10148_DA,
                     year_10148_ESD, year_10148_ID,
                     year_10148_NC, year_09119_BISM, year_09119_IDA,
                     year_09119_NC, year_09119_ESDA, year_09119_AIDA,
                     year_09119_MA, year_09119_ORA, year_09119_SA, year_09119_CPA, children=None):
            self._item_id = item_id
            self._name = name
            self._cp = cp
            self._item_type = item_type
            self._year_10143 = year_10143
            self._year_09019 = year_09019
            self._year_10148_BISM = year_10148_BISM
            self._year_10148_DA = year_10148_DA
            self._year_10148_ESD = year_10148_ESD
            self._year_10148_ID = year_10148_ID
            self._year_10148_NC = year_10148_NC
            self._year_09119_BISM = year_09119_BISM
            self._year_09119_IDA = year_09119_IDA
            self._year_09119_NC = year_09119_NC
            self._year_09119_ESDA = year_09119_ESDA
            self._year_09119_AIDA = year_09119_AIDA
            self._year_09119_MA = year_09119_MA
            self._year_09119_ORA = year_09119_ORA
            self._year_09119_SA = year_09119_SA
            self._year_09119_CPA = year_09119_CPA
            self._children = [] if children is None else children

        def code(self):
            if self._item_type == '':
                return self._item_id
            if self._item_type == 'c':
                return self._item_type + self._item_id
            else:
                return self._item_type.upper() + self._item_id


        def get_year_10143(self):
            return self._year_10143

        def get_year_09019(self):
            return self._year_09019

        def get_year_10148_BISM(self):
            return self._year_10148_BISM

        def get_year_10148_DA(self):
            return self._year_10148_DA

        def get_year_10148_ESD(self):
            return self._year_10148_ESD

        def get_year_10148_ID(self):
            return self._year_10148_ID

        def get_year_10148_NC(self):
            return self._year_10148_NC

        def get_year_09119_BISM(self):
            return self._year_09119_BISM

        def get_year_09119_IDA(self):
            return self._year_09119_IDA

        def get_year_09119_NC(self):
            return self._year_09119_NC

        def get_year_09119_ESDA(self):
            return self._year_09119_ESDA

        def get_year_09119_AIDA(self):
            return self._year_09119_AIDA

        def get_year_09119_MA(self):
            return self._year_09119_MA

        def get_year_09119_ORA(self):
            return self._year_09119_ORA

        def get_year_09119_SA(self):
            return self._year_09119_SA

        def get_year_09119_CPA(self):
            return self._year_09119_CPA

        def get_years(self):
            return {'Bachelor of Information Technology': self.get_year_10143(),
                    'Bachelor of Science (Honours) in Information Technology': self.get_year_09019(),
                    'Business Information Systems Management in Bachelor of Science in Information Technology': self.get_year_10148_BISM(),
                    'Data Analytics in Bachelor of Science in Information Technology': self.get_year_10148_DA(),
                    'Enterprise Systems Development in Bachelor of Science in Information Technology': self.get_year_10148_ESD(),
                    'Interaction Design in Bachelor of Science in Information Technology': self.get_year_10148_ID(),
                    'Networking and Cybersecurity in Bachelor of Science in Information Technology': self.get_year_10148_NC(),
                    'Business Information Systems Management in Bachelor of Computing Science (Honours)': self.get_year_09119_BISM(),
                    'Interaction Design in Bachelor of Computing Science (Honours)': self.get_year_09119_IDA(),
                    'Networking and Cybersecurity in Bachelor of Computing Science (Honours)': self.get_year_09119_NC(),
                    'Enterprise Systems Development in Bachelor of Computing Science (Honours)': self.get_year_09119_ESDA(),
                    'Artificial Intelligence and Data Analytics in Bachelor of Computing Science (Honours)': self.get_year_09119_AIDA(),
                    'Mathematical Analysis in Bachelor of Computing Science (Honours)': self.get_year_09119_MA(),
                    'Operations Research in Bachelor of Computing Science (Honours)': self.get_year_09119_ORA(),
                    'Statistics in Bachelor of Computing Science (Honours)': self.get_year_09119_SA(),
                    'Cybersecurity and Privacy in Bachelor of Computing Science (Honours)': self.get_year_09119_CPA()}

        def just_code(self):
            return self._item_id

        def get_search_list(self):
            return [[self._name, self._item_id]]

        def get_name(self):
            return self._name

        def get_type(self):
            return type_dict[self._item_type].lower()

        def get_children(self):
            return self._children

        def url(self):
            if self._item_type == '':
                return 'https://handbook.uts.edu.au/subjects/' + self._item_id + '.html'
            else:
                return 'https://handbook.uts.edu.au/directory/' + self.code() + '.html'

        def matches(self, id):
            return self._item_id == id or extract_digits(self._item_id) == extract_digits(id)

        def is_type(self, type):
            return self._item_type == type

        def cp(self):
            if self._cp is '':
                total = 0
                for child in self._children:
                    print(self.code())
                    print(child.code())
                    print(child.cp())
                    total += child.cp()
                return total
            else:
                return int(self._cp)

        def __repr__(self):
            return (str(int(self.cp())) + 'cp').rjust(2 + cp_length) + ' ' + \
                   (self.code()).rjust(id_length) + ' ' + self._name

        def display(self):
            tem = ''
            if not self.is_type('xbk'):
                tem += self.__repr__() + '\n'
            if self._cp is not '':
                tem += 'Select ' + self._cp + 'cp from options\n'
            for child in self._children:
                if child.is_type('xbk'):
                    tem += textwrap.indent(child.display(), '\t')
                else:
                    tem += '\t' + child.__repr__() + '\n'
            return tem

        def add_child(self, child):
            self._children.append(child)

    class Course(Substructure):
        def __init__(self, item_id, name, atar, hons, prof_prac, combined, location, other_names=None, children=None):
            super().__init__(item_id, name, 'c', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', [] if children is None else children)
            self._other_names = [] if other_names is None else other_names
            self._atar = atar if atar != '' else None
            self._hons = True if hons == '1' else False
            self._prof_prac = True if prof_prac == '1' else False
            self._combined = True if combined == '1' else False
            self._location = location

        def url(self):
            return 'http://handbook.uts.edu.au/courses/' + self.code() + '.html'

        def get_search_list(self):
            return super().get_search_list() + [[o, self._item_id] for o in self._other_names]

        def get_atar(self):
            return self._atar

        def is_hons(self):
            return self._hons

        def is_prof_prac(self):
            return self._prof_prac

        def is_combined(self):
            return self._combined

        def get_location(self):
            return self._atar

        def __repr__(self):
            return ('c' + str(self._item_id)).rjust(3 + cp_length + id_length) + ' ' + self._name

        def display(self):
            tem = self.__repr__()
            for item in self.items:
                tem += textwrap.indent(item.__repr__())
            return tem

        def add_alt_name(self, name):
            self._other_names.append(name)

    def __init__(self, cpath = None, ipath = None, rpath = None, npath = None):
        self._substructures = []
        _cpath = default_cpath if cpath is None else default_cpath
        _ipath = default_ipath if ipath is None else default_ipath
        _rpath = default_rpath if rpath is None else default_cpath
        _npath = default_npath if npath is None else default_npath
        self.load_csv(_cpath, _ipath, _rpath, _npath)

    def add(self, substructure):
        self._substructures.append(substructure)

    def add_substructure(self, item_id, name, item_type, cp, year_10143,
                         year_09019, year_10148_BISM, year_10148_DA,
                         year_10148_ESD, year_10148_ID, year_10148_NC,
                         year_09119_BISM, year_09119_IDA, year_09119_NC,
                         year_09119_ESDA, year_09119_AIDA, year_09119_MA,
                         year_09119_ORA, year_09119_SA, year_09119_CPA):
        self._substructures.append(self.Substructure(item_id, name, item_type, cp, year_10143,
                                                     year_09019, year_10148_BISM, year_10148_DA,
                                                     year_10148_ESD, year_10148_ID, year_10148_NC,
                                                     year_09119_BISM, year_09119_IDA, year_09119_NC,
                                                     year_09119_ESDA, year_09119_AIDA, year_09119_MA,
                                                     year_09119_ORA, year_09119_SA, year_09119_CPA))

    def add_course(self, item_id, name, atar, hons, prof_prac, combined, location):
        self._substructures.append(self.Course(item_id, name, atar, hons, prof_prac, combined, location))

    def __getitem__(self, key):
        tem = next((s for s in self._substructures if s.matches(str(key))), None)
        if tem is None:
            raise KeyError(str(key) + ' does not exist in this directory.')
        return tem

    def __setitem__(self, key, item):
        tem = [s for s in self._substructures if not s.matches(str(key))]
        self._substructures = tem
        self.add(item)

    def add_relation(self, key, key2):
        id1 = self.__getitem__(key)
        id2 = self.__getitem__(key2)
        if id1 is not None and id2 is not None:
            id1.add_child(id2)

    def add_alt_name(self, key, name):
        item_id = self.__getitem__(key)
        if item_id is not None:
            item_id.add_alt_name(name)

    def load_csv(self, cpath, ipath, rpath, npath=None):
        with open(cpath, 'r') as c:
            reader = csv.DictReader(c)
            for row in reader:
                self.add_course(row['id'],
                               row['name'],
                               row['atar'],
                               row['hons'],
                               row['prof_prac'],
                               row['combined'],
                               row['location'])

        with open(ipath, 'r') as i:
            reader = csv.DictReader(i)
            for row in reader:
                self.add_substructure(row['id'],
                                      row['name'],
                                      row['type'],
                                      row['cp'],
                                      row['year_10143'],
                                      row['year_09019'],
                                      row['year_10148_BISM'],
                                      row['year_10148_DA'],
                                      row['year_10148_ESD'],
                                      row['year_10148_ID'],
                                      row['year_10148_NC'],
                                      row['year_09119_BISM'],
                                      row['year_09119_IDA'],
                                      row['year_09119_NC'],
                                      row['year_09119_ESDA'],
                                      row['year_09119_AIDA'],
                                      row['year_09119_MA'],
                                      row['year_09119_ORA'],
                                      row['year_09119_SA'],
                                      row['year_09119_CPA'],
                                      )

        with open(rpath, 'r') as r:
            reader = csv.DictReader(r)
            for row in reader:
                self.add_relation(row['id'], row['id2'])

        if npath is not None:
            with open(npath, 'r') as r:
                reader = csv.DictReader(r)
                for row in reader:
                    self.add_alt_name(row['id'], row['name'])

    def courses(self):
        return [c for c in self._substructures if isinstance(c, self.Course)]

    def of_type(self, item_type):
        return [sb for sb in self._substructures if not sb.is_type(item_type)]

    def subjects(self):
        return [sb for sb in self._substructures if sb.is_type('')]

    def all(self):
        return [sb for sb in self._substructures if not sb.is_type('xbk')]

    def search_list(self, course_only = False):
        search_list = []
        for sb in self._substructures:
            if isinstance(sb, self.Course):
                search_list += sb.get_search_list()
            if not course_only and not sb.is_type('xbk'):
                search_list += sb.get_search_list()
        return search_list

    def search(self, query):
        search_list = self.search_list(str.upper(query.split(' ', 1)[0]) == 'BACHELOR')
        matches = [item_id for name, item_id in search_list if str.upper(name) == str.upper(query)]
        if len(matches) == 0:
            close_matches = get_close_matches(str.upper(query), [str.upper(name) for name, item_id in search_list])
            for c in close_matches:
                matches += [item_id for name, item_id in search_list if str.upper(name) == str.upper(c)]
        matches = list(set(matches))
        match_list = [[item_id, next((s.get_name() for s in self._substructures if s.matches(str(item_id))), None)] for
                      item_id in matches]
        return match_list

    def export_entities(self, path):
        entities = [name for name, item_id in self.search_list()]
        with open(path, 'w') as file:
            writer = csv.writer(file, delimiter='\n')
            writer.writerow(entities)
