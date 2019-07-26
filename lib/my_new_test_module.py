#!/usr/bin/python

ANSIBLE_METADATA = {
        'metadata_version': '1.1',
        'status': ['preview'],
        'supported_by': 'community'
}
DOCUMENTATION = '''
---
module: my_new_test_module

short_description: This is my sample

version_added: "2.4"

description:
- "Longer desc"

options:
    name:
        description: 
            - This is Message to send
        required: true
    new: 
        description: 
            - Control to demo
        required: false
    author:
    - Jimmy
'''

EXAMPLES = '''
# Pass in a message
- name: Test with message
  my_new_test_module:
    name: hello world

# Pass in a message and changed true
- name: Test with message and changed output
  my_new_test_module:
    name: hello world
    new: true

# Fail the module
- name: Test failure of the  module 
  my_new_test_module:
    name: fail me
'''

RETURN = '''
original_message:
    description: The original name param that was passwd in
    type: str
message:
    description: output
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define avail
    module_args = dict(
            name=dict(type='str', required=True),
            new=dict(type='bool', required=False, default=False)
    )
    
    result = dict(
            changed=False,
            original_message='',
            message=''
    )

    module = AnsilbleModule(
            argument_spec=module_args,
            supports_check_mode=True
    )

    if module.check_mode:
        return result

    result['original_message'] = module.params['name']
    result['message'] = 'gooddye'

    if module.param['new']:
        result['changed'] = True

    if module.param['name'] == 'fail me':
       module.fail_json(msg='You requrested this to fail', **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()



    

