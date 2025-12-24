from ingest_sds import ingest

text_by_section = {
    "Section 4": """
    FIRST AID MEASURES

    Inhalation:
    Move person to fresh air.

    Skin Contact:
    Wash with soap and water.

    Eye Contact:
    Rinse cautiously with water for several minutes.

    Ingestion:
    Do not induce vomiting.
    """
}

ingest(text_by_section)
