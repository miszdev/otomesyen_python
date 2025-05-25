import pytest
from tugas4 import book_train_ticket

@pytest.mark.slow
def test_book_train_ticket_runs_without_error():
    """
    Test dasar untuk memastikan fungsi berjalan tanpa error.
    Perlu ChromeDriver dan koneksi internet.
    """
    try:
        book_train_ticket("JAKARTA", "BANDUNG", 0)
    except Exception as e:
        pytest.fail(f"Fungsi gagal dijalankan: {e}")
