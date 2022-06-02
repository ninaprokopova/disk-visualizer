import shutil


class DiskInfo:
    """Возвращает информацию о диске"""

    def get_info_about_disk(self, path: str) -> (float, float):
        """Возвращает информацию о памяти диска path"""
        usage = shutil.disk_usage(path)

        return (usage.free, usage.used)
