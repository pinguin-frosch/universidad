package com.example.evaluacion3gabrielbarrientos;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import com.example.evaluacion3gabrielbarrientos.dao.DaoUsuario;
import com.example.evaluacion3gabrielbarrientos.dao.Usuario;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.ValueEventListener;

public class MainActivity extends AppCompatActivity {

    // Declarar los inputs de los elementos
    private EditText etRun, etNombre, etCorreo;

    // Declarar el listView y el adaptador
    private ListView lvUsuarios;
    private ArrayAdapter<Usuario> adaptador;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Asignar cada elemento con los del xml
        etRun = findViewById(R.id.run);
        etNombre = findViewById(R.id.nombre);
        etCorreo = findViewById(R.id.correo);
        lvUsuarios = findViewById(R.id.listView);

        // Configurar el adaptador
        adaptador = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1);

        // Vincular el adaptador con el listView
        lvUsuarios.setAdapter(adaptador);

        // Leer datos en tiempo real
        DaoUsuario dao = new DaoUsuario();
        dao.getReferencia().orderByChild("nombre").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                // Limpiar el adaptador antes de agregar datos
                adaptador.clear();

                // Añadir todos los usuarios
                for (DataSnapshot usuarioActual : snapshot.getChildren()) {
                    Usuario usuario = usuarioActual.getValue(Usuario.class);
                    if (usuario != null) {
                        String run = usuarioActual.getKey();
                        run = run.replace("|", ".");
                        usuario.setRut(run);
                        adaptador.add(usuario);
                    }
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });
    }

    public void insertarUsuario(View view) {
        // Obtener el run y verificar que sea válido
        String run = etRun.getText().toString();
        if (run.equals("")) {
            Toast.makeText(this, "El run no puede estar vacío", Toast.LENGTH_SHORT).show();
            return;
        }

        // Reemplazar los . en el un porque no se pueden usar en firebase directamente
        run = run.replace(".", "|");

        // Obtener el nombre y verificar que sea válido
        String nombre = etNombre.getText().toString();
        if (nombre.equals("")) {
            Toast.makeText(this, "El nombre no puede estar vacío", Toast.LENGTH_SHORT).show();
            return;
        }

        // Obtener el correo y verificar que sea válido
        String correo = etCorreo.getText().toString();
        if (correo.equals("")) {
            Toast.makeText(this, "El correo no puede estar vacío", Toast.LENGTH_SHORT).show();
            return;
        }

        // Insertar el usuario en firebase
        Usuario usuario = new Usuario(run, nombre, correo);
        DaoUsuario dao = new DaoUsuario();
        dao.insertarUsuario(usuario);

        // Limpiar los EditText
        etRun.setText("");
        etNombre.setText("");
        etCorreo.setText("");

        // Mostrar mensaje de inserción exitosa
        Toast.makeText(this, "Usuario registrado / actualizado", Toast.LENGTH_SHORT).show();
    }

    public void eliminarUsuario(View view) {
        // Obtener el run y verificar que sea válido
        String run = etRun.getText().toString();
        if (run.equals("")) {
            Toast.makeText(this, "El run no puede estar vacío", Toast.LENGTH_SHORT).show();
            return;
        }

        // Reemplazar los . en el un porque no se pueden usar en firebase directamente
        run = run.replace(".", "|");

        // Crear un usuario que solo incluya el run
        Usuario usuario = new Usuario();
        usuario.setRut(run);

        // Eliminar el contacto usando dao
        DaoUsuario dao = new DaoUsuario();
        dao.eliminarUsuario(usuario);

        // Limpiar los EditText
        etRun.setText("");
        etNombre.setText("");
        etCorreo.setText("");

        // Mostrar mensaje de eliminación exitosa
        Toast.makeText(this, "Usuario eliminado", Toast.LENGTH_SHORT).show();
    }
}