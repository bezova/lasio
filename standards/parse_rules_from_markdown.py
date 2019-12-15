import inspect
from hashlib import blake2b
from pathlib import Path

from lxml import etree
import markdown

from lasio.spec.specbase import Specification


print("from specbase import Specification\n\n\n")


class TemporaryRule:
    def __init__(self, spec_type, name, link, version):
        self.spec_type = spec_type
        self.name = name
        self.link = link
        self.version = version

    def name_hash(self):
        return blake2b(f"{self.name}_{self.version}".encode("ascii"), digest_size=4).hexdigest()
    
    def version_hash(self):
        return f"{float(self.version):.1f}".replace(".", "")

    def spec_name(self):
        return f"{self.spec_type}_{self.name_hash()}_V{self.version_hash()}"

    def as_stub(self):
        return f"""class {self.spec_name()}(Specification):
    '''{self.name}.

    Link to the relevant part of the Log ASCII Standard specification:

    {self.link}

    '''
    spec_type = "{self.spec_type}"
    spec_version = {float(self.version):.1f}

"""

rules = []
with open(Path(__file__).parent / "specifications.md", "r") as f:
    html = markdown.markdown(f.read())
    root = etree.fromstring("<html>" + html.replace("<code>", '"').replace("</code>", '"') + "</html>")
    for child in root:
        if child.tag == "h2":
            current_version = child.text.split()[1]
        if child.tag == "ul":
            for list_item in [c for c in child if c.tag == "li"]:
                child_links = [i for i in list_item if i.tag == "a"]
                first_link = child_links[0]

                if "Requirement:" in list_item.text:
                    rule_type = "Requirement"
                elif "Recommendation:" in list_item.text:
                    rule_type = "Recommendation"
                rules.append(
                    TemporaryRule(
                        spec_type=rule_type, 
                        name=first_link.text, 
                        link=first_link.get("href"),
                        version=current_version,
                    )
                )

for rule in sorted(rules, key=lambda x: x.spec_name()):
    print(rule.as_stub())
