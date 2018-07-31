import yaml
import json
import os
import re
import pprint

class Environment(object):
  """docstring for Environment"""
  def __init__(self):
    super(Environment, self).__init__()
    self.dir_path = os.path.dirname(os.path.realpath(__file__))
    self.tests_path = os.path.dirname(self.dir_path)
    self.config_file = os.path.join(self.dir_path, 'config.yml')
    if not os.path.exists(self.config_file):
      print("Not found config file %s"%(self.config_file))
      exit()
    else:
      self.config_raw = yaml.load(open(self.config_file, 'r'))
      self.config = self.__config(self.config_raw)

  def __config(self, config):
    all_config = {**config, **config['env_list'][config['env']]}
    all_config.pop(config['env'], None)
    all_config.pop('env_list', None)
    if ('eth' in all_config) and ('contract' in all_config['eth']):
      all_config['eth']['contract']['address'] = all_config['contract']
    return all_config

  def factory(self, file_name):
    file = os.path.join(self.tests_path, 'factory', file_name)
    if not os.path.exists(file):
      return False
    else:
      file_str = open(file, 'r')
      if re.search('\.yml$', file):
        return yaml.load(file_str)
      elif re.search('\.json$', file):
        with file_str as f:
          return json.load(file_str)
      else:
        return file_str

  def users(self):
    return self.factory('users.yml')

  def user(self):
    return self.users()[0]

  def factory_path(self, file_name):
    return os.path.join(self.tests_path, 'factory', file_name)

  def overwrite_factory(self, file_name, file_data):
    file = self.factory_path(file_name)
    stream = open(file, 'w')
    yaml.dump(file_data, stream)
    return file

  def save_factory(self, file_name, file_data):
    file = self.factory_path(file_name)
    if os.path.exists(file):
      stream = open(file_name, 'r')
    else:
      stream = open(file_name, 'w+')
    raw_data = yaml.load(stream)
    if isinstance(raw_data, dict):
      new_data = {**raw_data, **file_data}
    elif isinstance(raw_data, list):
      raw_data.append(file_data)
      new_data = raw_data
    else:
      new_data = file_data
    return self.overwrite_factory(file_name, new_data)
