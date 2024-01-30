---
- name: Query an Open API
  hosts: localhost
  connection: local

  vars:
      majortom: 'http://api.citybik.es/v2/networks'

  tasks:
  - name: Send an HTTP GET to API
    ansible.builtin.uri:
      method: GET
      url: "{{ majortom }}"
    register: data

  - name: Use debug to show what is inside of our variable
    ansible.builtin.debug:
      msg: "{{ data }}"

  - name: Slice the variable further to only return the JSON
    ansible.builtin.debug:
      msg: "{{ data.get('json') }}"

  - name: Use debug with a loop across the JSON data
    ansible.builtin.debug:
      msg: "On the {{ item.get('company') }} is: {{ item.get('name') }}"
    loop: "{{ data.get('json').get('people') }}"

