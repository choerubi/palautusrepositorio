import toml
from urllib import request
from project import Project

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        toml_data = toml.loads(content)
        print(toml_data)
        
        name = toml_data.get("tool").get("poetry").get("name")
        description = toml_data.get("tool").get("poetry").get("description")
        license = toml_data.get("tool").get("poetry").get("license")
        authors = toml_data.get("tool").get("poetry").get("authors")

        dependencies_in_dict = toml_data.get("tool").get("poetry").get("dependencies")
        dev_dependencies_in_dict = toml_data.get("tool").get("poetry").get("group").get("dev").get("dependencies")

        dependencies = list(dependencies_in_dict.keys())
        dev_dependencies = list(dev_dependencies_in_dict.keys())
        
        return Project(name, description, license, authors, dependencies, dev_dependencies)