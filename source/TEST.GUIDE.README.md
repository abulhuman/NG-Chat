# Testing Fixture Guide

When creating a `test/` dir inside any app, use the package structure below:
```
<package_name>
    |-- __init__.py
    |-- <...other_packages...>
    |-- tests
          |-- fixtures
                |-- __init__.py
                |-- <package_name>.py
          |-- __init__.py
          |-- test_<test_name/target>.py
```
For example, if `<package_name>=accounts` inside `accounts/tests/fixtures/accounts.py` would look like:

```doctest
import pytest
from model_bakery import baker

from source.general.utils.cryptography import KeyPair


@pytest.fixture
def sender_key_pair(): # [ℹ️] fixture #1
    return KeyPair(
        public='eb01f474a637e402b44407f3c1044a0c4b59261515d50be9abd4ee34fcb9075b',
        private='acb34653559abebeabf67e01c89ab5f0859674c8a643b294b9ffc89012ac2e2e'
    )


@pytest.fixture
def sender_account_number(sender_key_pair): # [ℹ️] fixture #2
    return sender_key_pair.public # ⬅️ fixture #1 usage


@pytest.fixture
def sender_account(sender_account_number, db): # [ℹ️] fixture #3
    return baker.make('accounts.Account', account_number=sender_account_number, balance=20000) # ⬅️ fixture #2 usage
```

Then you can use these fixtures inside your `test_<test_name/target>.py` files.  
For example, if we want to test `<URL>/api/account/:account_number` we can create a file `accounts/tests/test_retrieve_account.py` and inside it would look like:
```python
def test_should_successfully_retrieve_account(sender_account, api_client): # ⬅️ fixture #3 usage
    response = api_client.get(f'/api/accounts/{sender_account.account_number}')
    assert response.status_code == 200
    assert response.json() == {
        'account_number': sender_account.account_number,
        'balance': sender_account.balance,
        'display_image': '',
        'display_name': '',
    }
```