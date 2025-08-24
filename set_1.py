def savings(gross_pay, tax_rate, expenses):
    return ((gross_pay - int(gross_pay * tax_rate))- expenses)
def material_waste(total_material, material_units, num_jobs, job_consumption):
    return str(total_material - (num_jobs * job_consumption)) + str(material_units)
def interest(principal, rate, periods):
    return int(principal + (principal*rate*periods)) 