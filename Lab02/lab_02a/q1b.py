from q1a import Student
if __name__ == "__main__":
    student_list = [ ]
    student_list.append( Student( "310567", "Cheung Siu Ming" ) )
    student_list.append( Student( "451267", "Ng Wai Man" ) )
    student_list.append( Student( "789014", "Wong Sui Kai" ) )

    student_list[0].set_score( 87.1 )
    student_list[1].set_score( 77.5 )
    student_list[2].set_score( 83.4 )

    average_score = 0
    for i in range( len( student_list ) ):
        student_list[i].display_student()
        average_score += student_list[ i ].get_score()
    average_score = average_score / len( student_list )
    print( f"Average Score = {average_score:.2f}" )