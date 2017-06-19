from django.test import TestCase

# Create your tests here.
import ansible.runner
import ansible.inventory
import json

aa={"bb":{"hosts":["127.0.0.1"]}}
ip=ansible.inventory.Inventory("host")
print ip

runner=ansible.runner.Runner(host_list="hosts",module_name="shell",module_args="echo 11",remote_user="hujie",remote_pass="aixocm",inventory=ip)
print runner.run()
