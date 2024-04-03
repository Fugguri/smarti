from .BaseTokenSaverSource import BaseTokenSaverSource
import gspread
from .models.records import RecordRow


class GoogleSheetsSource(BaseTokenSaverSource):
    def __init__(self, source_url: str, project_name: str, project_id: int, service_account: str = "credentials.json") -> None:
        super().__init__(source_url, project_name, project_id)

        self.gc = gspread.service_account(service_account)
        self.sheet = self.gc.open_by_url(self.source_url).sheet1

    def _get_record(self, project_id: str | int = None, project_name: str = None, *args, **kwargs) -> RecordRow:
        record = None
        if project_name:
            record = self.sheet.find(self.project_name, case_sensitive=False)
        elif project_id:
            record = self.sheet.find(self.project_id, case_sensitive=False)

        if not record:
            record = self._create_record()
        row = self.sheet.row_values(record.row)
        return RecordRow(*row, record.row)

    def _save(self, project_id: int | str = None, project_name: str = None, tokens=None):
        record: RecordRow = self._get_record(
            project_id=project_id, project_name=project_name)
        record.token3 = int(record.token3) + tokens
        self.sheet.update_cell(record.row, 3, record.token3)
        return record

    def save(self, project_id: int | str = None, project_name: str = None, tokens=None):
        return self._save(project_id, project_name, tokens)

    def _create_record(self):
        self.sheet.append_row(
            self.project_name, self.project_id, 0, 0, 0)
        return self._get_record()

    def update_record(self):
        ...


if __name__ == "__main__":
    ...
