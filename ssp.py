import uuid
import datetime
import json

from oscal_pydantic import (
    catalog,
    assessment_plan,
    assessment_results,
    complete,
    component,
    poam,
    profile,
    ssp,
)

cg_uuid=uuid.uuid5(uuid.NAMESPACE_DNS, 'cloud.gov')

ssp_au_01 = ssp.SpecificControlStatement(
    statement_id="au_01_smt",
    uuid = str(uuid.uuid5(cg_uuid, 'ssp_au_01')),
    remarks = "This is a remark"
)

print(ssp_au_01.json())
