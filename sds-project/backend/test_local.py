from sds_service import process_sds_query

result = process_sds_query(
    query="What are the first aid measures?",
    product="ESPL-30-Seconds-Nzl-En-090625-1"
)

print("\n===== SDS RESPONSE =====")
print(result)
