package_pencils = int (input())
package_markes = int (input())
liters_of_preparat = int (input())
percent_discount = int (input())

total_pencils = package_pencils * 5.80
total_markers = package_markes * 7.20
total_preparat = liters_of_preparat * 1.20

total_sum = total_pencils + total_markers +total_preparat
total_sum = total_sum - (total_sum * percent_discount / 100 )
print (total_sum)