ANSIBLE_CONFIG=test/ansible.cfg ansible-playbook -i test/hosts -v test/playbook.yml "$@"
