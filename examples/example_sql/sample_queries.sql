
/*
**************
Sample Queries
**************
*/


SELECT order_taxon_name, family_name, genus_name FROM genus
JOIN family on genus.family_id=family.family_id
JOIN order_taxon on family.order_id=order_taxon.order_id
WHERE order_taxon_name="Anura" and family_name="Microhylidae";
