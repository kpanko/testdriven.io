import os
import tempfile

import pytest

from blog.models import Article


@pytest.fixture(autouse=True)
def database():
    fh, file_name = tempfile.mkstemp()
    os.environ["DATABASE_NAME"] = file_name
    Article.create_table(database_name=file_name)
    yield
    os.close(fh)
    os.unlink(file_name)
