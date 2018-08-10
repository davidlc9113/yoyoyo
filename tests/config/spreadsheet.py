import csv
import os
import pytest, ast

class Speadsheet(object):
  """docstring for Speadsheet"""
  def __init__(self, file_name):
    super(Speadsheet, self).__init__()
    self.file_name = file_name
    if os.path.exists(self.file_name):
      self.file = self.file_name
    else:
      dir_path = os.path.dirname(os.path.realpath(__file__))
      tests_path = os.path.dirname(dir_path)
      root_path = os.path.dirname(tests_path)
      self.file = os.path.join(root_path, file_name)
    self.rows = self.__rows(self.file)

  def __rows(self, file):
    _rows = []
    with open(file, 'r', newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        _rows.append(row)
    return _rows

  def overwrite(self, file_data):
    with open(self.file, 'w') as csvfile:
      fieldnames = list(self.rows[0].keys())
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
      print(file_data)
      for e in file_data:
        print(e)
        writer.writerow(e)
    return self.file

  def update(self, instances):
    print('')
    new_rows = []
    for e in self.rows:
      print(e['Title'])
      _dict = {}
      for x in ['Params', 'Assert Code']:
        _dict[x] = ast.literal_eval(e[x])
      response = getattr(instances[e['Instance']], e['Method'])(_dict['Params'])
      new_rows.append(e.copy())
      new_cols = {
        'Result': '',
        'Actual Time': response.time(),
        'Actual Response Code': response.code,
        'Actual Response Body': response.body()
      }
      for k, v in new_cols.items():
        new_rows[-1][k] = v
    self.file = self.overwrite(new_rows)
    print('')
    return self.file

  def update_result(self, instances):
    self.update(instances)
    self.rows = self.__rows(self.file)
    new_rows = []
    for e in self.rows:
      new_rows.append(e.copy())
      if 'Assert Code' in e and e['Assert Code']:
        if not isinstance(e['Assert Code'], list):
          e['Assert Code'] = [e['Assert Code']]
        if e['Actual Response Code'] in e['Assert Code']:
          new_rows[-1]['Result'] = 'Pass'
        else:
          new_rows[-1]['Result'] = 'Fail'
      if 'Assert Body' in e and e['Assert Body']:
        e['Assert Body'] = ast.literal_eval(e['Assert Body'])
        e['Actual Response Body'] = ast.literal_eval(e['Actual Response Body'])
        if e['Actual Response Body'].items() >= e['Assert Body'].items():
          new_rows[-1]['Result'] = 'Pass'
        else:
          new_rows[-1]['Result'] = 'Fail'
    self.file = self.overwrite(new_rows)
    return self.file

  def test(self, instances):
    self.update(instances)
    self.update_result(instances)
    self.rows = self.__rows(self.file)
    for e in self.rows:
      if e['Result']:
        assert e['Result'] == 'Pass'
