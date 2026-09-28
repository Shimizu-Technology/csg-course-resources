class CreatePracticeSessions < ActiveRecord::Migration[8.1]
  def change
    create_table :practice_sessions do |t|
      t.string :topic
      t.integer :minutes
      t.date :occurred_on

      t.timestamps
    end
  end
end
